import React, { Component } from 'react';
import { StyleSheet, Text, ScrollView } from 'react-native';
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
        textAlign: "center"
    }
});

export default class EventListView extends Component {
    render() {
        return (
            <ScrollView style={{ backgroundColor: '#d8dfea' }}>
                <Text style={{ textAlign: "center", fontSize: 20, marginTop: 35, fontWeight: 'bold' }}>
                    Events
                </Text>
                <Card
                    image={require('./assets/sf.jpg')}>
                    <Text style={{ textAlign: "center" }}>
                        Facebook Hackathon in San Francisco
                </Text>
                </Card>


                <Card
                    image={require('./assets/ny.jpg')}>
                    <Text style={{ textAlign: "center" }}>
                        Let's Learn Computer Vision! in Mountain View
                </Text>
                </Card>
                <Card
                    image={require('./assets/chicago.jpg')}>
                    <Text style={{ textAlign: "center" }}>
                        How to Build a Social Network in San Jose
                </Text>
                </Card>
                <Card
                    image={require('./assets/ucb.jpg')}>
                    <Text style={{ textAlign: "center" }}>
                        Community Hackathon in Berkeley
                </Text>
                </Card>
                <Card
                    image={require('./assets/fbhq.jpg')}>
                    <Text style={{ textAlign: "center" }}>
                        Maker Faire 2020 in Mountain View
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