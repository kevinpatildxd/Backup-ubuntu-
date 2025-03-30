import { createSlice, PayloadAction } from "@reduxjs/toolkit"
import { Pokemon } from "../../common/pokemon.model"

interface MyPokemonState {
  pokemons: Array<Pokemon>
}

const initialState: MyPokemonState = {
  pokemons: []
}

const slice = createSlice({
  name: 'myPokemon',
  initialState,
  reducers: {
    setPokemons: (state, action: PayloadAction<Array<Pokemon>>) => {
      state.pokemons = action.payload
      localStorage.setItem('myPokemons', JSON.stringify(action.payload))
    },
    syncMyPokemonLocalStorage: (state) => {
      const myPokemonsLS = localStorage.getItem('myPokemons')
      if (myPokemonsLS) {
        state.pokemons = JSON.parse(myPokemonsLS)
      }
    }
  }
})

export const { setPokemons, syncMyPokemonLocalStorage } = slice.actions

export default slice.reducer