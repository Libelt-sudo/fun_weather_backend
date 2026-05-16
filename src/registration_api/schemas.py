from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class UKPhoneNumber(PhoneNumber):

    default_region_code = 'GB'
    supported_regions   = ['GB']
    phone_format        = "INTERNATIONAL"



class SubscriberCreate(BaseModel):

    email:          EmailStr
    phone_number:   UKPhoneNumber




class SubscriberResponse(BaseModel):

    id:             int
    email:          EmailStr
    phone_number:   UKPhoneNumber
