import axios from 'axios'

export const BASE_URL = 'https://pokeapi.co/api/v2'

export const BASE_REQUEST =  {
  get: async function(url: string) {
    try {
      const response = await axios.get(url)
      return response.data;
    } catch(error: any) { 
      throw error;
    }
  }
}