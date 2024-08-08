# alert-sat-sample

Sample for setting up Stepfunctions, with Lambda, S3 and DDB

## Pre-requisites

- [Install AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

## Project overview

- `template.yaml`
  Cloudformation template (With the serverless transform activated, to enable writing shorter syntax for serverless resources, like Lambda, DDB etc.) For instance, [here's the docs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html) for the AWS::Serverless::Function resource (Lambda function). If you're ever in doubt just google the resource type (AWS::Serverless::Function, AWS::S3::Bucket etc) - the cloudformation documentation is really good.

- `functions/`
  Folder with all Lambda function code and dependencies

- `statemachine/inference_pipeline.asl.yaml`
  Yaml definition of stepfunction. I personally prefer to develop with YAML over json, but if you use the "designer" in the AWS console, you can inspect and/or export the JSON definition. You can use the JSON definition in here as well, or convert to YAML, which I have done.

- `samconfig.toml`
  This file contains metadata that the SAM cli uses when you use the different commands like `deploy`, `sync`, `logs` etc.

## Get started

to get started, run `sam build && sam deploy`. That will build and deploy everything to AWS.

## Nifty SAM commands

- `sam build`
  Installs all dependencies and creates the deployment artefact

- `sam deploy`
  Deploys the built artefact to AWS, using the parameters in the samconfig.toml

- `sam sync --watch`
  Starts a hot-reloading sync, watching for changes in the local project. Any saved changes are automatically synced with the live environment. Cloudformation changes trigger a build and deploy, which takes a few seconds. Lambda code changes are typically updated withing a second.

- `sam logs`
  Fetches cloudwatch logs from ALL Lambdas in the cloudformation stack

- `sam logs --tail`
  Same as above, but starts live tailing the logs

- `sam logs --filter XXX`
  Fetches only logs containing the string XXX. For instance `sam logs --filter ERROR`

- `sam logs --name XX`
  Fetches all the logs from the spcific function. For instance `sam logs --name PreprocessLambda`

- `sam delete`
  Deletes the cloudformation stack.

## Test

Test to upload the file:
`aws s3 cp test.txt s3://NAMEOFRAWBUCKET/test.txt`
then run `sam logs`.

#### Tip

My personal setup when I develop is one terminal with `sam sync --watch` running. In another window I have `sam logs --name XX --tail` running do watch the live logs.
