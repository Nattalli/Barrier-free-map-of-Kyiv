import React, { useEffect } from 'react';
import 'leaflet/dist/leaflet.css';
import 'leaflet-routing-machine/dist/leaflet-routing-machine.css';
import { MapContainer, TileLayer, Marker, Popup, useMapEvent } from 'react-leaflet'
import { Icon } from 'leaflet';
import 'leaflet-routing-machine';
import { createControlComponent } from '@react-leaflet/core';

const createRoutineMachineLayer = () => {
  const instance = (window.L as any).Routing.control({
    waypoints: [
      window.L.latLng(50.46845890135411, 30.515561699867252),
      window.L.latLng(50.46768916512869, 30.51419096125775),
      window.L.latLng([50.468523148153984, 30.512848825124244]),
      window.L.latLng([50.466608953519135, 30.51593858899743])
    ],
  });

  return instance;
};

const RoutingMachine = createControlComponent(createRoutineMachineLayer);

function MyComponent() {
  const map = useMapEvent('click', (event) => {
    console.log(event.latlng);
  });
  return null
}

type Geocode = [number, number];
type Point = {
  label: string;
  geocode: Geocode;
}

const calcDistance = (g1: Geocode, g2: Geocode) => Math.sqrt(Math.pow(g1[0] - g2[0], 2) + Math.pow(g1[1] - g2[1], 2)) * 100000;

const MIN_GRAPH_DISTANCE = 50;

const makeGraph = (points: Point[]) => {
  const graph = {} as any;
  points.forEach(currentPoint => {
    graph[currentPoint.label] = {};
    let haveConnection = false;
    let maxDistance = MIN_GRAPH_DISTANCE;
    while (!haveConnection) {
      points.forEach(neighborPoint => {
        if (currentPoint === neighborPoint) return;
        const distanceBetweenPoints = calcDistance(currentPoint.geocode, neighborPoint.geocode);
        if (distanceBetweenPoints < maxDistance) {
          graph[currentPoint.label][neighborPoint.label] = distanceBetweenPoints;
          haveConnection = true;
        }
      });
      maxDistance += 10;
    }
  });
  return graph;
}

export const MainPage = () => {
  // useEffect(() => {
  //   setTimeout(() => {
  //     (window.L as any).Routing.control({
  //       waypoints: [
  //         window.L.latLng(50.46869871698446, 30.515297493199174),
  //         window.L.latLng(50.46768916512869, 30.51419096125775)
  //       ]
  //     });
  //   }, 2000);
  // }, []);

  const customIcon = new Icon({
    iconUrl: 'https://cdn-icons-png.flaticon.com/512/149/149059.png',
    iconSize: [48, 48],
  });

  const points: Point[] = [
    { label: 'A', geocode: [50.46845890135411, 30.515561699867252] },
    { label: 'B', geocode: [50.46768916512869, 30.51419096125775] },
    { label: 'C', geocode: [50.468523148153984, 30.512848825124244] },
    { label: 'D', geocode: [50.46922639472987, 30.513925369453368] },
    { label: 'E', geocode: [50.46992963756902, 30.514980654685615] },
    { label: 'F', geocode: [50.466608953519135, 30.51593858899743] },
    { label: 'G', geocode: [50.46798394013522, 30.51810229287689] },
    { label: 'H', geocode: [50.46719725726207, 30.519486911985595] },
  ];

  console.log(makeGraph(points));

  return (
    <div style={{height: 500, width: 500}} id="map">
      <MapContainer center={[50.46869871698446, 30.515297493199174]} zoom={20} scrollWheelZoom={false}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {points.map((point, i) => (
          <Marker position={point.geocode} icon={customIcon} key={i}>
            <Popup>
              {point.label}
            </Popup>
          </Marker>
        ))}
        {/*<RoutingMachine />*/}
        <MyComponent />
      </MapContainer>
    </div>
  )
}