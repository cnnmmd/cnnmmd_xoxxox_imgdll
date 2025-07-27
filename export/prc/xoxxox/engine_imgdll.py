import os
import aiohttp
from openai import OpenAI
from xoxxox.shared import Custom

#---------------------------------------------------------------------------

class ImgPrc:
  def __init__(self, config="xoxxox/config_imgdll_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.nmodel = diccnf["nmodel"] # dall-e-3
    self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

  def status(self, config="xoxxox/config_imgdll_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.resimg = diccnf["resimg"] # 1024x1024
    self.quaimg = diccnf["quaimg"] # standard

  async def infere(self, prompt, promng):
    result = self.client.images.generate(
      model=self.nmodel,
      size=self.resimg,
      quality=self.quaimg,
      prompt=prompt,
      n=1,
    )
    urlimg = result.data[0].url
    async with aiohttp.ClientSession() as s:
      async with s.get(urlimg) as r:
        datimg = await r.read()
    return datimg
