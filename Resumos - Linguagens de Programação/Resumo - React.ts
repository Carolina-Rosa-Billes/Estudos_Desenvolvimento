import React from 'react'; //Importa o React para ser usado no código.

type?: tipo //Torna o tipo especificado opcional.

class Nome_Componente extends React.Component //Cria uma classe com um componente react. Pra chamar no app.tsx, colocar dentro da div como <Nome_Componente/>.
    {render()
        {return
            (<button>Nome do Botão </button>)}} //Nesse caso, o componente é um botão.

function Nome_Componente() //Cria uma função com um componente react. Pra chamar no app.tsx, colocar dentro da div como <Nome_Componente/>.
    {return
        (<button>Nome do Botão </button>)} //Nesse caso, o componente é um botão.

const array = [{ item: "Nome 1" }, { item: "Nome 2" }, { item: "Nome 3"}]; //Cria um aray renderizado automaticamente.
array.map(lista => <p> {array.item} </p>); //O que for adicionado no array será colocado, nesse caso, no parágrafo.

class Nome_Componente extends React.Component //Cria uma classe com um componente react e uma props. Pra chamar no app.tsx, colocar dentro da div como <Nome_Componente>Nome_Prop<Nome_Componente/>.
    {render()
        {return
            (<button>{this.props.children} </button>)}} //Nesse caso, o componente props é um botão.

function Nome_Funcao() //Cria uma função com vários componentes react, nesse caso, botões.
    {return
        (<>
            <button>Botão 1<button/>
            <button>Botão 2<button/>
            <button>Botão 3<button/>
        </>)}

function Nome_Funcao() //Cria uma função com componente react que atualiza automaticamente caso algo seja inserido no setItens.
    {const [itens, setItens] = useState
        ([{ item: "Nome 1" },
        { item: "Nome 2" },
        { item: "Nome 3"}]);
    return
        (setItens([{ item: "Nome 1" }, { item: "Nome 2" }, { item: "Nome 3"}, { item: "Nome 4"}]))}

