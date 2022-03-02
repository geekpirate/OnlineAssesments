
# return in a geographically sorted way Country > state > city > ....

input = [
    {
        'Id': 0,
        'location': 'Americas',
        'parentID': None
    },
    {
        'Id': 22,
        'location': 'Cali',
        'parentID': 2
    },
    {
        'Id': 3,
        'location': 'Detroit',
        'parentID': 0
    },
    {
        'Id': 211,
        'location': 'Ilionois',
        'parentID': 2
    },
    {
        'Id': 21,
        'location': 'Michigan',
        'parentID': 22
    },
    {
        'Id': 2,
        'location': 'US',
        'parentID': 0
    },
    {
        'Id': 11,
        'location': 'Britich Columbai',
        'parentID': 1
    },
    {
        'Id': 1,
        'location': 'Canada',
        'parentID': 0
    }
]
output = [
{
        'Id': 0,
        'location': 'Americas',
        'parentID': None
    },
    {
        'Id': 1,
        'location': 'Canada',
        'parentID': 0
    },
    {
        'Id': 11,
        'location': 'Britich Columbai',
        'parentID': 1
    },
    {
        'Id': 2,
        'location': 'US',
        'parentID': 0
    },
    {
        'Id': 22,
        'location': 'Cali',
        'parentID': 2
    },
    {
        'Id': 21,
        'location': 'Michigan',
        'parentID': 22
    },
    {
        'Id': 211,
        'location': 'Ilionois',
        'parentID': 2
    },
    {
        'Id': 3,
        'location': 'Detroit',
        'parentID': 0
    },
]

