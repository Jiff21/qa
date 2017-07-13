# Accessiblity

## Introduction

Test written using [Behave Framework](http://pythonhosted.org/behave/) and [Lighthouse](https://github.com/GoogleChrome/lighthouse)


## Install

Docker
```
docker pull matthiaswinkelmann/lighthouse-chromium-alpine
touch  accessibility/results.json
```

Run:

```
docker run -i matthiaswinkelmann/lighthouse-chromium-alpine --output json --output-path=results.json https://example.com
```

Or This seems to be docker command but 'sh: json: unknown operand' error is occurring
```
docker run -v $PWD/accessibility/results.json:/lighthouse/output/  -i matthiaswinkelmann/lighthouse-chromium-alpine --output json  https://example.com
```
