const http = require("http") //Diz que está sendo usado o http.
const port = process.end.PORT || 3000; //Especifica a porta que vai ser usada, nesse caso a 3000.

const rotas = //Cria uma constante para rotas. De acordo com o final do link, será mostrada uma mensagem.
    {"/": "Mensagem 1",
    "/2": "Mensagem 2",
    "/3": "Mensagem 3"}

const server = http.createServer((req, res) => { //Cria um servidor.
    res.writeHead(200, {"Content-Type": "text/plain"}); //Pede que seja um sucesso e devolva um texto.
    res.end(rotas[req.url])}) //E que esse texto é de acordo com a rota.

app.listen(port, () => { //Pede para ficar escutando a porta, as alterações.
  console.log(`Servidor escutando em http://localhost:${port}`)}) //E imprimir a mensagem.

const app = express(); //Põe o express numa variável, pra poder ser usado facilmente.
app.use(express.json()); //Converte os arquivos em json.

app.get("/", (req, res) => //Mostra o que fazer quando a rota for acessada, quando o final do link for /.
  {res.status(200).send("Mensagem")}) //Deve aparecer um sucesso com a mensagem.

app.post("/", (req, res) => //Adiciona um novo item em uma constante com vários.
    {nome_constante.push(req.body); //Empurra o novo item para o corpo da constante.
    res.status(201).send("Mensagem")}) //Mostra a mensagem, com sucesso.

app.put("/rota/:id", (req, res) => //Atualiza um elemento específico de uma rota.
  {let index = nome_função(req.params.id); //Busca o elemento, pelo id.
  nome_lista[index].titulo = req.body.titulo; //Substitui pelo passado no corpo da requisição.
  res.json(nome_lista)}) //E retorna o resultado como json.
    
function nome_função(id) //Busca na lista da rota o elemento específico, pelo id.
  {return nome_lista.findIndex(parametro => parametro.id == id)}; //Devolve essa lista, com o status 200.
    
app.delete("/rota/:id", (req, res) => //Deleta um elemento específico de uma rota.
  {let {id} = req.params; //Busca o elemento, pelo id.
  let index = nome_função(id);
  nome_lista.splice(index, 1); //Apaga ele, nesse caso só um elemento.
  res.send("Mensagem")}) //E retorna a mensagem.
    
mongoose.connect("link_banco_de_dados"); //Conecta o banco de dados com o node, através do moongose.
    
const nome_esquema = new mongoose.Schema //Cria um esquema.
  ({dado1: {type: tipo_dado1, required: true}, //Com o primeiro dado, nesse caso de preenchimento obrigatório.
  {dado2: {type: tipo_dado2}}) //E o segundo dado, de preenchimento opcional.
    
const nome_constante = mongoose.model(“nome_constante”, nome_esquema); //Torna o esquema o modelo pra preenchimento dos dados.
    
  class nome_controlador //Cria um controlador, um intermediário entre o banco de dados e o código node.
  {static nome = (req, res) =>
  {nome_lista.find((err, nome_lista) => //Busca na lista da rota o elemento específico, pelo id.
  { res.status(200).json(nome_lista)}; //Devolve essa lista, com o status 200.
    
const router = express.Router(); //Define o acontecimento para quando for no link com final ;.
  router.get("/", nome_controlador, nome_função);