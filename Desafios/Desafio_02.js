// Entrada de valores
let vitorias = 500
let derrotas = 5

// Fálculo do saldo e nível
let resultado = calculoNivel(vitorias, derrotas)

// Função
function calculoNivel (vitorias, derrotas){
    let saldoVitorias = vitorias - derrotas
    let nivel = ""

    if (vitorias < 10){
        nivel = "Ferro"
    } else if (vitorias >= 11 & vitorias <= 20){
        nivel = "Bronze"
    }else if (vitorias >= 21 & vitorias < 50){
        nivel = "Prata"
    }else if (vitorias >= 51 & vitorias < 80){
        nivel = "Ouro"
    }else if (vitorias >= 81 & vitorias < 90){
        nivel = "Diamante"
    }else if (vitorias >= 11 & vitorias < 20){
        nivel = "Bronze"
    }else if (vitorias >= 91 & vitorias < 100){
        nivel = "Lendário"
    }else{
        nivel = "Imortal"
    }
    return {saldoVitorias, nivel}
}

// Saída do resultado
console.log(" O herói tem um saldo de " + resultado.saldoVitorias + " e está no nívle " + resultado.nivel)