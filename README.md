# # Zuri Interns API Endpoint
"Exploring backend development with Zuri. Join my journey! 🐍🚀 #ZuriBackEndLearning" (80 characters)

Welcome to the Zuri Interns API Endpoint documentation. This API provides specific information in JSON format based on query parameters.

## Table of Contents

- [Objective](#objective)
- [Requirements](#requirements)
- [Acceptance Criteria](#acceptance-criteria)
- [Usage](#usage)
- [Testing](#testing)
- [Submission](#submission)
- [Submission Deadline](#submission-deadline)

## Objective

The objective of this API is to create and host an endpoint that takes two GET request query parameters and returns specific information in JSON format. The information includes Slack name, the current day of the week, current UTC time, track, GitHub file URL, GitHub repo URL, and a status code of success.

## Requirements

The API fulfills the following requirements:

- Provides a publicly accessible endpoint.
- Accepts two GET request query parameters: slack_name and track.
- Includes the slack_name passed as a GET request query parameter in the response.
- Displays the current day of the week.
- Returns the current UTC time within a +/-2 minute window.
- Displays the track based on the track GET parameter.
- Includes a direct link to the specific file in the GitHub repository that's being executed.
- Provides a link to the main page of the GitHub repository containing the project's entire source code.
- Returns a status code of 200.
- Formats the response in JSON.

## Acceptance Criteria

Before submission, make sure to:

- Ensure the endpoint is accessible.
- Check the returned JSON against the defined format.
- Validate the correctness of each data point in the JSON response.

## Usage

To use the API, make a GET request to the endpoint with the following query parameters:

- `slack_name`: Your Slack name.
- `track`: Your chosen track (e.g., "backend").

Example request:
