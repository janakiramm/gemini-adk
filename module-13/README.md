# Deployment Guide for Weather Time App

## Prerequisites

-   Google Cloud SDK installed and authenticated
-   `gcloud` CLI configured
-   `adk` CLI installed
-   A valid **GOOGLE_API_KEY** environment variable exported

------------------------------------------------------------------------

## 1. Create a Secret in Google Secret Manager

``` bash
echo $GOOGLE_API_KEY | gcloud secrets create GOOGLE_API_KEY --project=PROJECT_ID --data-file=-
```

------------------------------------------------------------------------

## 2. Grant Access to the Compute Service Account

``` bash
gcloud secrets add-iam-policy-binding GOOGLE_API_KEY --member="COMPUTE_SERVICE_ACCOUNT" --role="roles secretmanager.secretAccessor" --project="PROJECT_ID"
```

------------------------------------------------------------------------

## 3. Set Required Environment Variables

``` bash
export GOOGLE_CLOUD_PROJECT="PROJECT_ID"
export GOOGLE_CLOUD_LOCATION="us-central1"
export AGENT_PATH="./weather_time"
export SERVICE_NAME="weather-time"
export APP_NAME="weather_time_app"
```

------------------------------------------------------------------------

## 4. Deploy to Cloud Run Using ADK

``` bash
adk deploy cloud_run --project=$GOOGLE_CLOUD_PROJECT --region=$GOOGLE_CLOUD_LOCATION --service_name=$SERVICE_NAME --app_name=$APP_NAME --with_ui $AGENT_PATH
```

------------------------------------------------------------------------

## Notes

-   Ensure that the Agent Path (`./weather_time`) contains the required
    ADK agent files.
-   The `--with_ui` flag deploys the UI alongside the Cloud Run service.
-   Replace identifiers with your actual project details if deploying in
    a different environment.

------------------------------------------------------------------------

## Troubleshooting

-   Verify Secret Manager permissions if deployment fails to access
    `GOOGLE_API_KEY`
-   Ensure Cloud Run API is enabled:

``` bash
gcloud services enable run.googleapis.com
```
