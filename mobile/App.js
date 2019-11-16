import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import CameraView from './CameraView';
import LoginView from './LoginView';
import Swiper from 'react-native-swiper';

export default function App() {
  // return <LoginView />;
  // return <CameraView />;
  return (
    <Swiper loop={false}>
      <CameraView />
      <LoginView />
    </Swiper>
  )
}

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
// });
