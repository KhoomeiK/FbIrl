import React, { Component } from 'react';
import { StyleSheet, Text, ScrollView} from 'react-native';
// import { redBright } from 'ansi-colors';
import { Card } from 'react-native-elements';
// import LinearGradient from 'react-native-linear-gradient';

const styles = StyleSheet.create({
    container: {
      flex: 1,
      paddingTop: 22,
    //   borderColor: "black",
    },
    item: {
      padding: 10,
      fontSize: 18,
      height: 44,
      borderStyle: "solid",
      borderWidth: 1,
    //   marginBottom: 20,
      paddingTop: 30,
      paddingBottom: 50,
    //   width: "40%",
    //   marginLeft: "25%",
      textAlign: "center",
      color: "white",
      backgroundColor: "rgb(66,103,178)",
    },
    card: {
        textAlign:"center"
    }
  });

export default class EventListView extends Component {
    render() {
        return (
            <ScrollView style={styles.scrollView}>
            <Card></Card>
            {/* <LinearGradient colors={['#4c669f', '#3b5998', '#192f6a']}> */}
            <Card
                image={require('./assets/sf.jpg')}>
                <Text style={{textAlign:"center"}}>
                    Community Hackathon San Francisco
                </Text>
            </Card>
            {/* </LinearGradient> */}
            

            <Card
                image={require('./assets/ny.jpg')}>
                <Text style={{textAlign:"center"}}>
                    Community Hackathon New York
                </Text>
            </Card>
            <Card
                image={require('./assets/chicago.jpg')}>
                <Text style={{textAlign:"center"}}>
                    Community Hackathon Chicago
                </Text>
            </Card>
            <Card
                image={require('./assets/test.png')}>
                <Text style={{textAlign:"center"}}>
                    Community Hackathon Antarctica
                </Text>
            </Card>
            <Card
                image={require('./assets/test.png')}>
                <Text style={{textAlign:"center"}}>
                    Community Hackathon Space
                </Text>
            </Card>
            </ScrollView>
            
        );
    }
}


// export default class FlatListBasics extends Component {
//   render() {
//     return (
//       <View style={styles.container}>
//         <FlatList
//           data={[
//             { key: ['Hackathon SF', "sf.jpg"]},
//             { key: ['Hackathon NY', "assets/test.png"] },
//             { key: ['Hackathon Chi', "assets/test.png"]},
//           ]}
          
//         //   renderItem={({ item }) => <Button title={item.key} color="#f194ff" style = {styles.item}> </Button>}
//           renderItem={({ item }) => 
            
           
//             <Image
//                 // style={{width: "100%", height: "100%"}}
                
//                 source={require('../mobile/assets/sf.jpg')}
//             />

//           }
//         />
//       </View>


//     );
//   }
// }

// <Text style={styles.item} >{item.key}</Text>
// <Text style={styles.item} >{item.key[1]}</Text>