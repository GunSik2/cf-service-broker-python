import bottle
import requests
import json
import os
import logging

# UPDATE THIS FOR YOUR ECHO SERVICE DEPLOYMENT
service_base = "localhost:8081"  # echo-service.stackato.danielwatrous.com

@bottle.route('/echo/<instance_id>', method='PUT')
def echo_provision(instance_id):
    return {"sueccess"}

@bottle.route('/echo/<instance_id>', method='DELETE')
def echo_deprovision(instance_id):
    return {"sueccess"}

@bottle.route('/echo/<instance_id>/<binding_id>', method='PUT')
def echo_bind(instance_id, binding_id):
    return {"sueccess"}

@bottle.route('/echo/<instance_id>/<binding_id>', method='DELETE')
def echo_unbind(instance_id, binding_id):
    return {"sueccess"}

@bottle.route('/echo/dashboard/<instance_id>', method='GET')
def echo_dashboard(instance_id, binding_id):
    return {"sueccess"}

if __name__ == '__main__':
    port = int(os.getenv('PORT', '8081'))
    bottle.run(host='0.0.0.0', port=port, debug=True, reloader=False)
