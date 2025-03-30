import { BASE_REQUEST, BASE_URL } from "../../common/base.api"

const PokemonListApi: any = {
  getPokemonList: (limit = 20, offset = 0): Promise<any> => BASE_REQUEST.get(`${BASE_URL}/pokemon?limit=${limit}&offset=${offset}`)
}

export default PokemonListApi