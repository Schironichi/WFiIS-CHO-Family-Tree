from django.shortcuts import render, redirect
from django.contrib import messages
from neomodel import db
from .forms import PersonForm, RelationForm
from .models import Person


def home(req):
    context = {
        'people': Person.nodes.all(),
    }
    return render(req, 'tree/home.html', context)

def person(req, uid):
    personData = Person.nodes.filter(uid=uid)
    data = personData.first()
    
    if req.method == 'POST':
        form = PersonForm(req.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(req, 'Profile updated.')
            return redirect(req.META.get('HTTP_REFERER'))
    else:
        form = PersonForm(instance=data)
        
    siblings, meta = db.cypher_query("MATCH (:Person{uid:'" + data.uid + "'})-[:CHILD]->()-[:PARENT]->(p) WHERE NOT p.name IN ['" + data.name + "'] RETURN DISTINCT p")
    cousins, meta = db.cypher_query("MATCH (:Person{uid:'" + data.uid + "'})-[:CHILD]->(p1)-[:CHILD]->()-[:PARENT]->(p2)-[:PARENT]->(p) WHERE NOT p.name IN ['" + data.name + "'] AND p2 <> p1 RETURN DISTINCT p")
    grandparents, meta = db.cypher_query("MATCH (:Person{uid:'" + data.uid + "'})-[:CHILD]->()-[:CHILD]->(p) RETURN p")
    
    context = {
        'person': data,
        'form': form,
        'siblings': list(map(lambda x: Person.inflate(x[0]), siblings)),
        'cousins': list(map(lambda x: Person.inflate(x[0]), cousins)),
        'grandparents': list(map(lambda x: Person.inflate(x[0]), grandparents)),
    }
    return render(req, 'tree/person.html', context)

def newPerson(req):    
    if req.method == 'POST':
        form = PersonForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Profile created.')
            return redirect('tree-home')
        else:
            messages.warning(req, 'Error occured. Try again')
            return redirect('new-person')
    else:
        form = PersonForm()

    context = {
        'form': form,
    }
    
    return render(req, 'tree/new_person.html', context)

def newRelation(req):
    if req.method == 'POST':
        form = RelationForm(req.POST)
        if form.is_valid() and form.cleaned_data['person_from'] != form.cleaned_data['person_to']:
            person_from = Person.nodes.first(uid=form.cleaned_data['person_from'])
            person_to = Person.nodes.first(uid=form.cleaned_data['person_to'])
            if form.cleaned_data['relation'] == 'MARRIED':
                person_from.spouse.connect(person_to)
                person_to.spouse.connect(person_from)
            if form.cleaned_data['relation'] == 'PARENT':
                person_from.children.connect(person_to)
                person_to.parents.connect(person_from)
            if form.cleaned_data['relation'] == 'CHILD':
                person_from.parents.connect(person_to)
                person_to.children.connect(person_from)
            messages.success(req, 'Relation added.')
            return redirect('tree-home')
        else:
            messages.warning(req, 'Cannot add relation to the same person.')
            return redirect('new-relation')
        
    else:
        form = RelationForm()

    context = {
        'form': form,
    }
    
    return render(req, 'tree/new_relation.html', context)

def delPerson(req, uid):
    personData = Person.nodes.filter(uid=uid)
    data = personData.first()
    
    if req.method == 'POST':
        personData.first().delete()
        messages.success(req, 'Profile removed.')
        return redirect('tree-home')

    context = {
        'person': data,
    }
    
    return render(req, 'tree/person_confirm_delete.html', context)
