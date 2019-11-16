import React from 'react';

import { Text, View } from 'react-native';
import * as Permissions from 'expo-permissions';
import { Camera } from 'expo-camera';
import * as FaceDetector from 'expo-face-detector';
import axios from 'axios';

export default class CameraView extends React.Component {
  state = {
    hasCameraPermission: null,
    type: Camera.Constants.Type.back,
  };

  handleFaces = async obj => {
    if (obj.faces.length > 0 && !this.state.seeingFace) { // first time new face
      this.setState({ bounds: obj.faces[0].bounds, seeingFace: true })
      let photo = await this.camera.takePictureAsync({ quality: 0.5, base64: true })
      let content = {
        photo: photo.base64,
        x: this.state.bounds.origin.x,
        y: this.state.bounds.origin.y,
        width: this.state.bounds.size.width,
        height: this.state.bounds.size.height
      }
      let data = await axios.post('http://bdc01c4b.ngrok.io/classify', content)
      console.log(data.data)
    }
    else if (obj.faces.length > 0) { // continuing to adjust to new face
      this.setState({ bounds: obj.faces[0].bounds })
      // console.log(this.state.bounds)
    }
    else if (obj.faces.length === 0 && this.state.seeingFace) { // first time no face visible
      this.setState({ seeingFace: false })
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