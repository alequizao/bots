import requests, json
url = "http://api.sefaz.al.gov.br/sfz_nfce_api/api/public/consultarPrecosCombustivel"
payload = json.dumps({
  "codTipoCombustivel": "1",
  "dias": 1,
  "latitude": -9.6432331,
  "longitude": -35.7190686,
  "raio": 15
})

data = json.dumps({
  "codGetin": '',
  "codNcm": '',
  "dscProduto": "GAS COMUM",
  "valMinimoVendido": '',
  "valMaximoVendido": '',
  "dthEmissaoUltimaVenda": "2019-09-13T09:21:37.000+0000",
  "valUnitarioUltimaVenda": "4.279",
  "valUltimaVenda": "4.12851886711731",
  "numCNPJ": "47508411126338",
  "nomRazaoSocial": "COMPANHIA BRASILEIRA DE DISTRIBUICAO",
  "nomFantasia": '',
  "numTelefone": "(11) 38860599",
  "nomLogradouro": "AV  COMENDADOR GUSTAVO PAIVA",
  "numImovel": "3393",
  "nomBairro": "CRUZ DAS ALMAS",
  "numCep": "57038000",
  "nomMunicipio": "MACEIO",
  "numLatitude": "",
  "numLongitude":-35.7248617
  })

headers = {
  'Content-Type': 'application/json',
  'appToken': 'b7c64cae488c2f3fd4045bc940a9bfe627f3a10c'
}
response = requests.request("POST", url, headers=headers, data=payload).text
#print(response)
obj = json.loads(response)
#print(obj)
for i in obj:
  #print(f"{i}")
  print(f"Produto: {i['dscProduto']}")
  print(f"Hora da venda: {i['dthEmissaoUltimaVenda']}")
  print(f"Valor da venda: {i['valUnitarioUltimaVenda']}")
  print(f"Posto: {i['nomFantasia']}")
  print(f"Numero: {i['numTelefone']}")
  print(f"Endereço: {i['nomLogradouro']}, {i['numImovel']}, {i['nomBairro']}, {i['numCep']}, {i['nomMunicipio']}")
  print("*"*50,"<br>")

