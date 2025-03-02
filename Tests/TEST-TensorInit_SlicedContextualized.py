import requests
import sys
import os
import tempfile

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils.Defs.TensorInit_SlicedContextualized import TensorInit_SlicedContextualized

ConversationUsers=[
    {
        "id": "uid=1",
        "name": "アシスタント",
        "phonetic_jp": "アシスタント",
        "phonetic_en": "Assistant",
        "preferred_name": "アシスタント",
        "gender": "agender",
        "pronouns": "{ 'Jp':{ 'fpp': '私' }, 'En': { 'Sub': 'it', 'Obj': 'it', 'Pos': 'its', 'Ref': 'itself' } }",
        "bio": "Generic Personal AI Assistant"
    },
    {
        "id": "uid=5",
        "name": "山田・花子",
        "phonetic_jp": "やまだ・はなこ",
        "phonetic_en": "Yamada Hanako",
        "preferred_name": "花子",
        "gender": "woman",
        "pronouns": "{ 'Jp':{ 'fpp': '私' }, 'En': { 'Sub': 'she', 'Obj': 'her', 'Pos': 'hers', 'Ref': 'herself' } }",
        "bio": "Placeholder User. 花子 represents any user of the service."
    }
]

# Use the raw URL for direct file content
url = "https://raw.githubusercontent.com/Lexa-B/Ayaka_MS_EmoTensorGen/main/Configs/EmoList_Plutchik.xml"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a temporary file to store the XML content
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
        temp_file.write(response.text)
        temp_file_path = temp_file.name
    
    try:
        EmoTensor = TensorInit_SlicedContextualized(ConversationUsers, temp_file_path)
        #print(EmoTensor)
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)
else:
    print(f"Error downloading file: {response.status_code}")

with open("TEST-EmoTensor.etsc", "w") as f:
    f.write(EmoTensor.model_dump_json(indent=2))