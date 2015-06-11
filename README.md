# Preface #

This document describes the functionality provided by the xlr-polling-webhook-plugin.

See the **XL Release Reference Manual** for background information on XL Release and release concepts.

# Overview #

The xlr-polling-webhook-plugin provides functionality to poll a REST endpoint and check for a particular return value

## Types ##

+ PollingJSONWebHook
  * `URL`
  * `HTTP Method`
  * `HTTP Body`
  * `Username`
  * `Password`
  * `Proxy Host`
  * `JSON Path Expression` - JSON Path to find return value
  * `Target Value` - Target value for the JSON Path to return
  * `Polling Interval` - Interval to poll for
  * `Poll Count` - Number of times to poll before the task fails
  * `Continue On Timeout` - If checked task will not fail on timeout, allowing the release continue
  * `Value Found` - Output variable, will be set to the string 'True' if the value was found, string 'False' if not. Use if `Continue on Timeout` is checked.
