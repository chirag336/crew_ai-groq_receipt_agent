from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import io
from PIL import Image
import pytesseract


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "This is an OCR tool to extract text from PDFs"
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        img = Image.open("/content/airbnb.png").convert("RGB")
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        img = Image.open(io.BytesIO(img_byte_arr))

        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
        text = pytesseract.image_to_string(img)
        # del state['the_image']
        return {text}
