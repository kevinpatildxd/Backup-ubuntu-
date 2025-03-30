import React from 'react';
import { setHasMenu, setTitle } from '../../app-layout.slice';
import { useAppDispatch, useAppSelector } from '../../redux/hooks';
import { Box, Grid, Paper, Typography } from '@mui/material';
import { Link } from 'react-router-dom';
import { syncMyPokemonLocalStorage } from './my-pokemon.slice';

export function MyPokemon(): JSX.Element {

  // redux states
  const dispatch = useAppDispatch()
  const { pokemons } = useAppSelector(state => state.myPokemon)


  React.useEffect(() => {
    dispatch(setHasMenu(true))
    dispatch(setTitle("My Pokemon"))
    dispatch(syncMyPokemonLocalStorage())
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <Box  sx={{
        height: '90%',
        overflow: 'auto'
      }}>
        {
          pokemons.length > 0 ?
            <Box height="max-content" py={1} minHeight="100%" display="flex" flexDirection="column">
              <Grid container spacing={2} marginBottom={2}>
                {
                  pokemons.map((pokemon, index: number) => 
                    <Grid item key={index} xs={6} sm={4}>
                      <Link to={`/pokemon/${pokemon.name}?isCatchable=false`} style={{ textDecoration: 'none', color: 'inherit'}}>
                        <Paper sx={
                          {
                            px:1.5,
                            py:1
                          }
                        }>
                          <Typography variant="h2" fontSize={16} fontWeight="bold">{ pokemon?.nickname || "no nickname" }</Typography>
                          <Typography fontSize={13} fontWeight={500} color="text.secondary">species: <i>{pokemon.name}</i></Typography>
                        </Paper>
                      </Link>
                    </Grid>
                  ) 
                }
              </Grid>
            </Box>
          :
            <Box height="400px" display="flex" justifyContent="center" alignItems="center" flexDirection="column">
              <Typography paragraph sx={{ textAlign: 'center', maxWidth: '300px', fontWeight: 'bold', fontSize:14, color: 'text.secondary' }}>
                No results found
              </Typography>
            </Box>
        }        
    </Box>
  )
}