from django.http import Http404

from claim.models import Claim, ClaimWithDoc

def get_claim_class(doc: bool):
    if doc:
        return ClaimWithDoc
    else:
        return Claim

def param_check(param):
    if param == 'true':
        return True
    elif param == 'false':
        return False
    else:
        raise ValueError


def get_claim_object(id):
    try:
        return Claim.objects.get(id=id)
    except Claim.DoesNotExist:
        try:
            return ClaimWithDoc.objects.get(id=id)
        except ClaimWithDoc.DoesNotExist:
            raise Http404()

def get_client_profile(claim):
    return claim.client

def get_client_profile_from_claim(id):
    claim_obj = get_claim_object(id)
    return get_client_profile(claim_obj)