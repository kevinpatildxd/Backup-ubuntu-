import { Canvas } from '@react-three/fiber'
import './App.css'
import { Experience } from './components/Experience'

function App() {
  return (
    <Canvas camera={{ position: [2, 2, 2], fov: 60 }}>
      <Experience />
    </Canvas>
  )
}

export default App
