#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys, string, time
from com.xebialabs.xlrelease.plugin.webhook import JsonPathResult
from com.xebialabs.xlrelease.plugin.webhook import XmlPathResult
from urlparse import urlparse


def isJson():
    return 'jsonPathExpression' in globals()

def process(response, expression, ExpressionProcessor):
    result_expected = expression is not None and len(expression) > 0

    if result_expected:
        resultVariable = ExpressionProcessor(response, expression).get()
        if resultVariable is None:
            print "Expression %s did not match anything in the response" % expression
            sys.exit(1)
        print "Result: %s" % resultVariable
        return resultVariable

def process_json(response, jsonPathExpression):
    return process(response, jsonPathExpression, JsonPathResult)

def process_xml(response, xPathExpression):
    return process(response, xPathExpression, XmlPathResult)


if isJson():
    content_type = 'application/json'
else:
    print 'Could not determine Webhook format, JsonPath expression was not provided'
    sys.exit(1)

x = 0
while x < pollCount:
    uri = urlparse(URL)

    host = '%s://%s' % (uri.scheme, uri.netloc)
    context = uri.path

    if uri.query:
        context = '%s?%s' % (context, uri.query)

    server = { 'url': host, 'username': username, 'password': password, 'proxyHost': proxyHost, 'proxyPort': proxyPort}
    request = HttpRequest(server, username, password)

    if body is None:
        body = ""

    response = request.doRequest(method = method, context = context, body = body, contentType = content_type)

    if response.isSuccessful():
        if isJson():
            result = process_json(response.response, jsonPathExpression)
            if result == targetValue:
                print "Http Status: %s" % response.status
                print "JSON %s returned %s" % (jsonPathExpression, result)
                sys.exit(0)
            else:
                x += 1
                time.sleep(pollingInterval)
    else:
        print "Failed to connect at %s." % URL
        response.errorDump()
        sys.exit(1)

print "Poll count hit without %s found" % targetValue
sys.exit(1)
