import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import CameraView from './CameraView';
import LoginView from './LoginView';
import Swiper from 'react-native-swiper';

export default function App() {
  return (
    <Swiper loop={false}>
      <LoginView />
      <CameraView />
    </Swiper>
  )
}