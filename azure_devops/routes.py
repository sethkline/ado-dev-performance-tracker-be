from flask import Blueprint, jsonify
import os
import requests
import base64
from models.goal import Goal

azure_devops_bp = Blueprint('azure_devops', __name__)

def get_azure_devops_data():
    pat = os.environ.get('AZURE_DEVOPS_PAT')
    if not pat:
        raise ValueError("AZURE_DEVOPS_PAT environment variable is not set.")
    encoded_bytes = base64.b64encode((':' + pat).encode('utf-8'))
    encoded_pat = str(encoded_bytes, 'utf-8')

    organization = os.environ.get('AZURE_DEVOPS_ORG')
    project = os.environ.get('AZURE_DEVOPS_PROJECT')
    project_id = os.environ.get('AZURE_DEVOPS_PROJECT_ID')
    repository_id = os.environ.get('AZURE_DEVOPS_REPOSITORY_ID')
    base_url = os.environ.get('AZURE_DEVOPS_BASE_URL')
    creator_id = os.environ.get('AZURE_DEVOPS_CREATOR_ID')

    headers = {'Authorization': f'Basic {encoded_pat}'}
    # url = f"{base_url}/{organization}/_apis/projects?api-version=2.0"
    # url = f"{base_url}/{organization}/{project}/_apis/git/repositories/{repository_id}/pullrequests?api-version=7.1-preview.1"
    url = f"{base_url}/{organization}/{project_id}/_apis/git/repositories/{repository_id}/pullRequests?searchCriteria.creatorId={creator_id}&searchCriteria.status=3"
    # url = f"{base_url}/{organization}/_apis/Contribution/HierarchyQuery/project/{project_id}"
    

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

@azure_devops_bp.route('/data')
def get_data():
    try:
        data = get_azure_devops_data()
        return jsonify(data)  # Send JSON response
    except Exception as e:
        return {"error": str(e)}, 500
    
@azure_devops_bp.route('/goals')
def show_goals():
    goals = Goal.query.all()
    return jsonify([{'id': goal.id, 'title': goal.title, 'description': goal.description} for goal in goals])

