import { OrbitControls } from '@react-three/drei'

export const Experience = () => {
  return (
    <>
      <OrbitControls />
      <mesh>
        <boxGeometry args={[1, 1, 1]} />
        <meshNormalMaterial />
      </mesh>
    </>
  )
}
