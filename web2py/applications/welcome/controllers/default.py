# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def post():
    sensor = request.vars['sensor']
    reading = request.vars['reading']
    table = db.readings
    table.insert(sensor=sensor, reading=reading)




def todo():

    category = request.vars['category']
    summary = request.vars['summary']
    description = request.vars['description']
    phone_id = request.vars['phone_id']
    
    table = db.todo
    table.insert(category=category, summary=summary, description=description, phone_id=phone_id)
    db.commit()
    
   
def todoview():
    table = db.todo
    table.id.readable = False
    query = (table.id>0)
    form = SQLFORM.grid(query=query, paginate=25)
    return dict(form=form)


def get_ip():


    loc_ip = request.vars['loc_ip']
    ext_ip = request.vars['ext_ip']
    sysinfo = request.vars['sysinfo']
    
    table = db.pi_ip
    if table.insert(loc_ip=loc_ip, ext_ip=ext_ip, sysinfo=sysinfo, time_stamp=request.now):
        return "Logged.Thanks!"
    

def ip_view():

    table = db.pi_ip
    table.id.readable = False
    query = (table.id>0)
    form = SQLFORM.grid(query=query, paginate=25, orderby=~table.id)
    return dict(form=form)
