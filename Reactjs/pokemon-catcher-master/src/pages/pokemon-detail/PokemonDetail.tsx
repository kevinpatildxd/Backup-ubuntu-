import React from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import { setHasMenu, setTitle } from '../../app-layout.slice';
import { useAppDispatch, useAppSelector } from '../../redux/hooks';
import { getPokemon, saveToMyPokemon, setError } from './pokemon-detail.slice';
import { Box, CircularProgress, Table, TableBody, TableCell, TableRow, Typography, Fab, Snackbar, Alert, Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions, DialogContentText } from '@mui/material';
import CatchingPokemonIcon from '@mui/icons-material/CatchingPokemon';

interface SnackbarState {
  isOpen: boolean,
  type: "info" | "warning" | "success" | "error",
  message: string
}

export function PokemonDetail(): JSX.Element {
  const params = useParams()
  let [searchParams] = useSearchParams()

  // redux states
  const { pokemon, isLoading, error } = useAppSelector(state => state.pokemonDetail)
  const dispatch = useAppDispatch()
  React.useEffect(() => {
    dispatch(setTitle(''))
    dispatch(setHasMenu(false))  
    if(params.species) {
      dispatch(getPokemon(params.species))
    } else {
      dispatch(setError('Please supply the Pokemon name in url path!'))
    }
  }, [params.species]) // eslint-disable-line react-hooks/exhaustive-deps

  // local states
  const [snackbar, setSnackbar] = React.useState<SnackbarState>({ isOpen: false, type: 'info', message: ''})
  const [isCatchable, setIsCatchable] = React.useState<boolean>(true)
  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false)
  const [pokemonNickname, setPokemonNickname] = React.useState<string>('')
  const [isCatchingLoading, setIsCatchingLoading] = React.useState<boolean>(false)

  const catchPokemon = () => {
    setIsCatchingLoading(true)
    setTimeout(() => {
      // 255 is the capture rate number. see https://pokeapi.co/docs/v2#pokemon-species
      // if the capture rate doesn't exist, the capture rate value set to 127.5 (50%)
      const catchNumber = Math.floor(Math.random() * 255)
      const isCaught = catchNumber <= (pokemon?.species?.capture_rate || 127.5)
      console.log(`Capture rate: ${pokemon?.species?.capture_rate} / 255 \nCatch number: ${catchNumber} \nPokemon will be captured if catch number <= ${pokemon?.species?.capture_rate}`)
      if (isCaught) {
        setSnackbar({ isOpen: true, type: 'success', message: `${pokemon?.name} is captured` })
        setIsModalOpen(true)
      } else {
        setSnackbar({ isOpen: true, type: 'error', message: `Failed to capture ${pokemon?.name}. Try again!` })
      }     
      setIsCatchingLoading(false) 
    }, 1500)
  }

  const saveCaughtPokemon = () => {
    const nicknamedPokemon = JSON.parse(JSON.stringify(pokemon));
    nicknamedPokemon.nickname = pokemonNickname
    dispatch(saveToMyPokemon(nicknamedPokemon))
    setSnackbar({ isOpen: true, type: 'success', message: `${pokemon?.name} is saved to My Pokemon collection` })
    setIsModalOpen(false)
    setIsCatchable(false)
  }

  const closeSnackbar = (event: any, reason: string = '') => {
    if (reason === 'clickaway') {
      return;
    }
    setSnackbar({ isOpen: false, type: 'info', message: ''})
  }

  const closeModal = (event: any, reason: string = '') => {
    if (reason === 'backdropClick') {
      return;
    }
    setIsModalOpen(false)
  }

  React.useEffect(() => {
    setPokemonNickname(pokemon ? pokemon?.name + Math.floor(Math.random() * 100) : '')
    if (searchParams.has('isCatchable')) {
      setIsCatchable(searchParams.get('isCatchable') !== 'false')
    }
  }, [pokemon]) // eslint-disable-line react-hooks/exhaustive-deps

  return (
      <Box sx={{
          height: '100%',
          overflow: 'auto'
        }}>
          {
            isLoading ?
              <Box height="100%" display="flex" justifyContent="center" alignItems="center" flexDirection="column">
                <CircularProgress />
              </Box>
            :
              error ?
                <Box height="100%" display="flex" justifyContent="center" alignItems="center" flexDirection="column">
                  <Typography paragraph sx={{ textAlign: 'center', maxWidth: '300px', fontSize:14, color: 'error.main' }}>
                    {error}
                  </Typography>
                </Box>
              :
                pokemon ?
                  <Box minHeight="100%" height="max-content" pb="50px">
                    <Box p={2} display="flex" justifyContent="center" alignItems="center" flexDirection="column">
                      <img src={pokemon.sprites.other.dream_world.front_default || ''} alt={pokemon.name} width="200" style={{ marginBottom: '15px'}}/>
                      <Typography variant="h3" fontSize={21} fontWeight="bold" textTransform="capitalize">{pokemon.name}</Typography>
                      <Typography paragraph fontSize={14} textTransform="capitalize">
                        Types: {
                          pokemon.types.map((type: any, index: number) => (pokemon.types.length === index + 1) ? `${type.type.name}` : `${type.type.name}, `)
                        }
                      </Typography>
                    </Box>
                    <Box>
                      <Table size="small">
                        <TableBody>
                          {
                            pokemon.stats.map((stat: any, index: number) => 
                              (
                                <TableRow key={index}>
                                  <TableCell sx={{textTransform: 'capitalize', fontWeight: 'bold', whiteSpace: 'nowrap'}}>{stat.stat?.name}</TableCell>
                                  <TableCell align="right">{stat.base_stat}</TableCell>
                                </TableRow>
                              )
                            )
                          }
                          <TableRow>
                            <TableCell sx={{textTransform: 'capitalize', fontWeight: 'bold', verticalAlign: 'top'}}>Moves</TableCell>
                            <TableCell align="right">
                              {
                                pokemon.moves.map((move: any, index: number) => (pokemon.moves.length === index + 1) ? `${move.move.name}` : `${move.move.name}, `)
                              }
                            </TableCell>
                          </TableRow>
                        </TableBody>
                      </Table>
                    </Box>

                    <Fab 
                      disabled={!isCatchable}
                      color="error"
                      variant="extended"
                      aria-label="Catch"
                      sx={{ position: 'fixed', left: '50%', transform: 'translateX(-50%)', bottom: '20px', whiteSpace: 'nowrap', minWidth: '250px'}}
                      onClick={catchPokemon}
                    >
                      {
                        !isCatchable ?
                          <div style={{ position: 'absolute', left: 0, bottom: 0, right: 0, top: 0, background: '#eee', zIndex: '0', borderRadius: '30px'}}>
                          </div>
                        : null
                      }
                      {
                        !isCatchingLoading ?
                          <div style={{ display: 'flex', zIndex: '1'}}>
                            <CatchingPokemonIcon sx={{ mr: 1 }}/> Catch this Pokemon
                          </div>
                        :
                          <div style={{ display: 'flex', zIndex: '1', textTransform: 'capitalize', justifyContent: 'center', alignItems: 'center'}}>
                            <CircularProgress size={30} color="inherit" sx={{ mr: 1 }} />
                            <span>
                              { (pokemon?.species?.capture_rate / 255 * 100).toFixed(2) + '% success chance'}
                            </span>
                          </div>
                      }
                    </Fab>
                    
                    <Snackbar
                      open={snackbar.isOpen}
                      onClose={closeSnackbar}
                      autoHideDuration={5000}
                      anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
                      >
                        {
                          snackbar.isOpen ?
                            <Alert onClose={closeSnackbar} severity={snackbar.type} sx={{ width: '100%' }}>
                              {snackbar.message}
                            </Alert>
                          : <div></div>
                        }
                      </Snackbar>
                      <Dialog
                        // fullScreen={true}
                        open={isModalOpen}
                        onClose={closeModal}
                        aria-labelledby="modal-modal-title"
                        aria-describedby="modal-modal-description"
                        sx={{width: '100%'}}
                        PaperProps={{ style: { margin: '15px'} }}
                        >
                          <DialogTitle>Add to My Pokemon</DialogTitle>
                          <DialogContent>
                            <DialogContentText>
                              Please give a nickname for your pokemon before adding it to your collection. You can also release it again.
                            </DialogContentText>
                            <TextField
                              required
                              autoFocus
                              margin="dense"
                              id="nickname"
                              label="Nickname"
                              type="text"
                              value={pokemonNickname}
                              onChange={(e) => setPokemonNickname(e.target.value)}
                              fullWidth
                              variant="standard"
                            />
                          </DialogContent>
                          <DialogActions>
                            <Button color="error" onClick={closeModal}>Release & Close</Button>
                            <Button onClick={saveCaughtPokemon}>Save</Button>
                          </DialogActions>
                      </Dialog>
                  </Box>
                : null
          }
      </Box>
        
  )
}