
from aiogram import Router, types, F
import random
rt = Router()
@rt.message(F.text.lower() == "it")
async def it(msg: types.Message):
    rasmlar = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGEgZNh2WAUizKH_VM3oYtUlinXqjNTgisU6QOdGazFA&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh0tW1NRLNQFsZ6So9qqOdV89u6FYQl07f87lcZG_6_w&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4B4KuAd0gGPxTI6HoIkVfoymuoPUVn_NW0K4IkiOLhw&s=10"
    ]

    rasm = random.choice(rasmlar)
    await msg.answer_photo(photo=rasm)
