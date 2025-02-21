class heroi{
    constructor(nome, idade, tipo,){
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }
    atacar(){
        let ataque;

        switch (this.tipo.toLowerCase()){
            case "mago":
                ataque = "magia"
                break;
            case "guerreiro":
                ataque = "espada"
                break;
            case "monge":
                ataque = "artes marciais"
                break;
            case "ninja":
                ataque = "shuriken"
                break;
            default:
                ataque = "ataque desconhecido"
    }
    console.log(`O ${this.tipo} atacou usando ${ataque}`)
  }
}

let heroi1 = new heroi ("Harry",150,"mago")
heroi1.atacar()
let heroi2 = new heroi ("Sancho",30,"guerreiro")
heroi2.atacar()
let heroi3 = new heroi ("Lee",40,"monge")
heroi3.atacar()
let heroi4 = new heroi ("SubZero",25,"ninja")
heroi4.atacar()