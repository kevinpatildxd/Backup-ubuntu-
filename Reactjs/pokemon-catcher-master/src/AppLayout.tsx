import React from 'react';
import { NavLink, useLocation } from "react-router-dom";
import { ThemeProvider, createTheme, Container, Grid, Box, Tab, Breakpoint, Typography } from '@mui/material'
import CssBaseline from "@mui/material/CssBaseline";
import TravelExploreIcon from '@mui/icons-material/TravelExplore'
import PetsIcon from '@mui/icons-material/Pets'
import { useAppSelector } from './redux/hooks'

interface AppLayoutProps {
  children: React.ReactNode
}

interface Menu {
  path: string,
  icon: JSX.Element,
  label: String
}

export default function AppLayout({ children }: AppLayoutProps): JSX.Element {
  const location = useLocation()
  const { title, hasMenu } = useAppSelector(state => state.appLayout)
  const [containerWidth, setContainerWidth] = React.useState<Breakpoint>('xs')

  const theme = createTheme({
      palette: {
        mode: 'light'
      },
      components: {
        MuiCssBaseline: {
          styleOverrides: {
            body: {
              backgroundColor: '#ededed',
            }
          }
        }
      }
    })

  React.useEffect(() => {
    setContainerWidth((window.innerWidth > 500) ? 'md' : 'xs')
    function handleResize() {
      setContainerWidth((window.innerWidth > 500) ? 'md' : 'xs')
    }
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const menus: Menu[] = [
    {
      path: '/',
      icon: <TravelExploreIcon fontSize="small"/>,
      label: 'Wild Pokemon'
    },
    {
      path: '/my-pokemon',
      icon: <PetsIcon fontSize="small"/>,
      label: 'My Pokemon'
    }
  ]

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container 
        maxWidth={containerWidth}
        sx={{
          margin: '0 auto',
          height: '100vh',
          bgcolor: 'background.default',
          p: 2,
          position: 'relative',
          overflow: 'hidden',
          fontSize: 14
        }}>
          <Grid container justifyContent="space-between" alignItems="center">
            <Grid item>
              {
                title !== '' ?
                  <Typography variant="h3" fontSize={20} fontWeight="bold">{title}</Typography>
                :
                  <NavLink to="/">
                    <TravelExploreIcon sx={{ color: 'text.secondary' }} />
                  </NavLink>
              }
            </Grid>
          </Grid>
          <Box sx={{
            height:'95%',
            py: 1
          }}>
            { children }
          </Box>
          {
            hasMenu ?
            <Grid container 
              zIndex={999} 
              bgcolor={theme.palette.background.paper}
              borderTop={`1px solid ${theme.palette.divider}`} 
              justifyContent="center" 
              position="absolute" bottom={0} left={0} right={0}>
              {
                menus.map((menu, i) => (
                  <Grid key={i} item xs={6} textAlign="center">
                    <NavLink
                      key={i}
                      to={menu.path}
                      style={({ isActive }) => ( isActive || (i === 0 && location.pathname === '/') ? { textDecoration: 'none', color: `${theme.palette.primary.dark}` } : { textDecoration: 'none', color: `${theme.palette.text.secondary}` })}
                    >
                      <Tab icon={menu.icon} label={menu.label} style={{ width: '100%', opacity: '1', fontSize: '14px', fontWeight: '500', textTransform: 'capitalize' }}/>
                    </NavLink>
                  </Grid>
                ))
              }
            </Grid>
            : ''
          }
      </Container>
    </ThemeProvider>
  )
}