
export interface Pokemon {
  id: number,
  name: string,
  height: number,
  weight: number,
  order: number,
  base_experience: number,
  is_default: boolean,
  abilities: PokemonAbility[],
  moves: PokemonMove[],
  forms: PokemonForm[],
  game_indices: PokemonGameIndice[],
  species: PokemonSpecies,
  sprites: PokemonSprites,
  stats: PokemonStat[],
  types: PokemonType[],
  owned?: number,
  nickname?: string
}

export interface PokemonSummary {
  name: string,
  string: string,
  owned?: number
}

export interface PokemonSpecies {
  id: number,
  name: string,
  base_happiness: number,
  capture_rate: number,
  color: PokemonSummary,
  habitat: PokemonSummary,
  has_gender_differences: boolean,
  hatch_counter: number,
  is_baby: boolean,
  is_legendary: boolean,
  is_mythical: boolean,
  url?: string
}

interface PokemonForm {
  name: string,
  string: string
}

interface PokemonGameIndice {
  game_index: number,
  version: any,
}

interface PokemonMove {
  move: object,
  version_group_details: Array<any>
}

interface PokemonAbility {
  ability: any,
  is_hidden: boolean,
  slot: number
}

interface PokemonSprites {
  back_default: string | null,
  back_female: string | null,
  back_shiny: string | null,
  back_shiny_female: string | null,
  front_default: string | null,
  front_female: string | null,
  front_shiny: string | null,
  front_shiny_female: string | null,
  other: PokemonOtherSprites,
  versions: any
}

interface PokemonOtherSprites {
  dream_world: PokemonSprites,
  home: PokemonSprites,
  "official-art": PokemonSprites
}

interface PokemonStat {
  base_stat: number,
  effort: number,
  stat: any
}

interface PokemonType {
  slot: number,
  type: any
}