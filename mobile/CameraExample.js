import React from 'react';

import { Text, View, Image } from 'react-native';
import * as Permissions from 'expo-permissions';
import { Camera } from 'expo-camera';
import * as FaceDetector from 'expo-face-detector';
import axios from 'axios';

export default class CameraExample extends React.Component {
  state = {
    hasCameraPermission: null,
    type: Camera.Constants.Type.back,

  };

  setStateAsync = state => {
    return new Promise(resolve => {
      this.setState(state, resolve)
    });
  }

  snap = async () => {
    if (this.camera) {
      let photo = await this.camera.takePictureAsync({ quality: 0.5 })
      console.log(photo)
      this.setState({ captured: photo })
    }
  }

  handleFaces = async obj => {
    if (obj.faces.length > 0 && !this.state.seeingFace) { // first time new face
      await this.setStateAsync({ bounds: obj.faces[0].bounds, seeingFace: true })
      console.log(this.state.bounds, this.state.seeingFace)
      await this.snap()
      let content = {
        photo: this.state.captured.base64,
        x: this.state.bounds.origin.x,
        y: this.state.bounds.origin.y,
        width: this.state.bounds.size.width,
        height: this.state.bounds.size.height
      }
      await axios.post('IP', content, () => console.log("You're ready for AR!")); // SET THIS IP
    }
    // else if (obj.faces.length > 0) { // continuing to adjust to new face
    //   await this.setStateAsync({ bounds: obj.faces[0].bounds })
    //   console.log(this.state.bounds)
    // } 
    else if (obj.faces.length === 0 && this.state.seeingFace) { // first time no face visible
      await this.setStateAsync({ seeingFace: false })
      console.log(obj.faces.length, this.state.seeingFace)
    }
  }

  async componentDidMount() {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({ hasCameraPermission: status === 'granted' });
  }

  render() {
    const { hasCameraPermission } = this.state;
    if (hasCameraPermission === null) {
      return <View />;
    } else if (hasCameraPermission === false) {
      return <Text>No access to camera</Text>;
    }
    // else if (this.state.captured) { // display captured image
    //   return <Image
    //     style={{ width: Math.floor(this.state.captured.width / 5), height: Math.floor(this.state.captured.height / 5) }}
    //     source={{ uri: this.state.captured.uri }}
    //   />
    // }
    else {
      return (
        <View style={{ flex: 1 }}>
          <Camera
            ref={ref => { this.camera = ref }}
            style={{ flex: 1 }} ratio='16:9' type={this.state.type}
            onFacesDetected={obj => this.handleFaces(obj)}
            faceDetectorSettings={{
              mode: FaceDetector.Constants.Mode.fast,
              detectLandmarks: FaceDetector.Constants.Landmarks.none,
              runClassifications: FaceDetector.Constants.Classifications.none,
              minDetectionInterval: 100,
              tracking: true,
            }}
          />
        </View>
      );
    }
  }
}