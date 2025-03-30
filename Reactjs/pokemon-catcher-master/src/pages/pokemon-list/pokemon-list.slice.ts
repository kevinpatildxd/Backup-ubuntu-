import { createSlice, PayloadAction } from "@reduxjs/toolkit"
import { Pokemon, PokemonSummary } from "../../common/pokemon.model"
import { AppThunk } from "../../redux/store"
import { syncMyPokemonLocalStorage } from "../my-pokemon/my-pokemon.slice"
import PokemonListApi from "./pokemon-list.api"

interface PokemonListState {
  limit: number,
  offset: number,
  totalCount: number,
  pokemons: Array<PokemonSummary|Pokemon>,
  isLoading: boolean,
  error: string | null
}

const initialState: PokemonListState = {
  limit: 18,
  offset: 0,
  totalCount: 0,
  pokemons: [],
  isLoading: false,
  error: null
}

const slice = createSlice({
  name: 'pokemonList',
  initialState,
  reducers: {
    startLoading: state => {
      state.isLoading = true
    },
    setPokemons: (state, action: PayloadAction<Array<PokemonSummary|Pokemon>>) => {
      state.pokemons = action.payload
      state.isLoading = false
    },
    setError: (state, action: PayloadAction<string>) => {
      state.error = action.payload
      state.isLoading = false
    },
    setOffset: (state, action: PayloadAction<number>) => {
      state.offset = action.payload
    },
    setTotalCount: (state, action: PayloadAction<number>) => {
      state.totalCount = action.payload
    }
  }
})

export const { startLoading, setPokemons, setError, setOffset, setTotalCount } = slice.actions

export const getPokemons = (): AppThunk => (dispatch, getStates) => {
  dispatch(startLoading())
  const limit = getStates().pokemonList.limit
  const offset = getStates().pokemonList.offset
  PokemonListApi.getPokemonList(limit, offset)
    .then((res: any) => {
      const markedCaughtPokemons = dispatch(markCaughtPokemons(res.results))
      dispatch(setPokemons(markedCaughtPokemons))
      dispatch(setTotalCount(res.count))
    })
    .catch((err: any) => {
      console.log(err)
      dispatch(setError(err?.message))
    })
}

const markCaughtPokemons = (pokemons: PokemonSummary[] | Pokemon[]): AppThunk<PokemonSummary[] | Pokemon[]> => (dispatch, getStates) => {
  dispatch(syncMyPokemonLocalStorage())
  const myPokemons: Pokemon[] = getStates().myPokemon.pokemons
  const pokemonsCopy: Pokemon[] = JSON.parse(JSON.stringify(pokemons))
  return pokemonsCopy.map((pokemon, index:number) => {
    const filteredMyPokemon = myPokemons.filter(myPokemon => myPokemon.name === pokemon.name)
    pokemon.owned = filteredMyPokemon.length
    return pokemon
  })
}

export const updateOwnedPokemon = (pokemon: Pokemon): AppThunk => (dispatch, getStates) => {
  const pokemons: Pokemon[] = JSON.parse(JSON.stringify(getStates().pokemonList.pokemons))
  const ownedPokemon: Pokemon = pokemons.find(p => p.name === pokemon.name) as Pokemon

  const myPokemons: Pokemon[] = JSON.parse(JSON.stringify(getStates().myPokemon.pokemons))
  const matchedMyPokemons: Pokemon[] = myPokemons.filter(p => p.name === pokemon.name)

  if(ownedPokemon)
    ownedPokemon.owned = matchedMyPokemons.length

  dispatch(setPokemons(pokemons))
}

export default slice.reducer