
from aiogram import Router, types, F
import random
rt = Router()
@rt.message(F.text.lower() == "mushuk")
async def mushuk(msg: types.Message):
    rasmlar = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGnKlPd0mp14qI90I_HnHyvIGMHrrFCxJBsOnfuNJn1Q&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRv45xpBzZm_e-StfaIElBEYm6oRpIxyt1bCm3OjIproA&s=10",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfPSEsp4DAKNEMSg5LYagTlB8TAs1BOy7A1Jxok797Fg&s=10"
    ]

    rasm = random.choice(rasmlar)
    await msg.answer_photo(photo=rasm)
