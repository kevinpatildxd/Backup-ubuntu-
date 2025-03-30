import React from 'react';
import { setHasMenu, setTitle } from '../../app-layout.slice';
import { useAppDispatch, useAppSelector } from '../../redux/hooks';
import { Box, CircularProgress, Grid, Pagination, Paper, Typography } from '@mui/material';
import { Link } from 'react-router-dom';
import { getPokemons, setOffset, setPokemons } from './pokemon-list.slice';

export function PokemonList(): JSX.Element {

  // redux states
  const dispatch = useAppDispatch()
  const { pokemons, isLoading, error, totalCount, limit, offset } = useAppSelector(state => state.pokemonList)

  // local states
  const [page, setPage] = React.useState<number>(1)

  const handlePageChange = (page: number) => {
    dispatch(setPokemons([]))
    setPage(page)
  }

  React.useEffect(() => {
    dispatch(setHasMenu(true))
    dispatch(setTitle("Let's catch wild pokemon"))
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  React.useEffect(() => {
    if (pokemons.length > 0) {
      setPage(offset / limit + 1)
    } else {
      dispatch(setOffset(page * limit - limit))
      dispatch(getPokemons())
    }
  }, [page]) // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <Box  sx={{
        height: '90%',
        overflow: 'auto'
      }}>
        {
          isLoading ?
            <Box height="100%" display="flex" justifyContent="center" alignItems="center" flexDirection="column">
              <CircularProgress />
            </Box>
          :
            pokemons.length > 0 ?
              <Box height="max-content" py={1} minHeight="100%" display="flex" justifyContent="center" alignItems="center" flexDirection="column">
                <Grid container spacing={2} marginBottom={2}>
                  {
                    pokemons.map((pokemon, index: number) => 
                      <Grid item key={index} xs={6} sm={4}>
                        <Link to={`pokemon/${pokemon.name}`} style={{ textDecoration: 'none', color: 'inherit'}}>
                          <Paper sx={
                            {
                              px:1.5,
                              py:1
                            }
                          }>
                            <Typography variant="h2" fontSize={16} textTransform="capitalize" fontWeight="bold">{ pokemon.name }</Typography>
                            <Typography fontSize={14} fontWeight={500} color="text.secondary">Owned: { pokemon?.owned ? <strong>{pokemon?.owned}</strong> : 0 }</Typography>
                          </Paper>
                        </Link>
                      </Grid>
                    ) 
                  }
                </Grid>
                <Pagination 
                  sx={{ mx: 'auto', mt: '7px', textAlign: 'center', width: 'max-content' }} 
                  color="primary" 
                  shape="rounded" 
                  count={Math.ceil(totalCount / limit)} 
                  page={page}
                  onChange={(event, page) => handlePageChange(page)} />
              </Box>
            :
              error ?
                <Box height="400px" display="flex" justifyContent="center" alignItems="center" flexDirection="column">
                  <Typography paragraph sx={{ textAlign: 'center', maxWidth: '300px', fontSize:14, color: 'error.main' }}>
                    Error occured when fetching pokemon data.<br/>
                    {error}
                  </Typography>
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