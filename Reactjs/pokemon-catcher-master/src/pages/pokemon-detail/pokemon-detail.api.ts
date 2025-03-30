import { BASE_REQUEST, BASE_URL } from "../../common/base.api"

const PokemonDetailApi: any = {
  getPokemonDetail: (name: string): Promise<any> => BASE_REQUEST.get(`${BASE_URL}/pokemon/${name}`),
  getPokemonSpecies: (name: string): Promise<any> => BASE_REQUEST.get(`${BASE_URL}/pokemon-species/${name}`)
}

export default PokemonDetailApi