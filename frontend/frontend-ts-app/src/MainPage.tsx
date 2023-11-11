import React, { useEffect, useState } from 'react';
import 'leaflet/dist/leaflet.css';
import 'leaflet-routing-machine/dist/leaflet-routing-machine.css';
import { MapContainer, TileLayer, Marker, Popup, useMapEvent } from 'react-leaflet'
import { Icon } from 'leaflet';
import 'leaflet-routing-machine';
import { createControlComponent } from '@react-leaflet/core';
import axios from "axios";
import Button from 'devextreme-react/button';
import { useNavigate } from 'react-router-dom';

const getMarkerIcon = (title: any) => title === 'Міжквартальні тротуари' ? new Icon({
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/98/98145.png',
  iconSize: [24, 24],
}) : new Icon({
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/149/149059.png',
  iconSize: [48, 48],
});

const getRouteMarkerIcon = () => new Icon({
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/149/149060.png',
  iconSize: [48, 48],
});

const createRoutineMachineLayer = (props: any) => {
  const instance = (window.L as any).Routing.control({
    waypoints: [
      props.startPoint,
      props.endPoint
    ],
    profile: 'foot',
  });

  return instance;
};

const RoutingMachine = createControlComponent(createRoutineMachineLayer);

function MapClickEvents({onMapClick}: any) {
  const map = useMapEvent('click', (event) => {
    onMapClick(event, map)
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
  const [points, setPoints] = useState<any[]>([]);
  const [isAddingNewPointMode, setAddingNewPointMode] = useState(false);
  const [isShowRouteMode, setRouteMode] = useState(false);
  const [startPoint, setStartPoint] = useState<any>();
  const [endPoint, setEndPoint] = useState<any>();

  const navigate = useNavigate();

  useEffect(() => {
    axios.get('/api/points').then(data => setPoints(data.data));
  }, []);

  // const points: Point[] = [
  //   { label: 'A', geocode: [50.46845890135411, 30.515561699867252] },
  //   { label: 'B', geocode: [50.46768916512869, 30.51419096125775] },
  //   { label: 'C', geocode: [50.468523148153984, 30.512848825124244] },
  //   { label: 'D', geocode: [50.46922639472987, 30.513925369453368] },
  //   { label: 'E', geocode: [50.46992963756902, 30.514980654685615] },
  //   { label: 'F', geocode: [50.466608953519135, 30.51593858899743] },
  //   { label: 'G', geocode: [50.46798394013522, 30.51810229287689] },
  //   { label: 'H', geocode: [50.46719725726207, 30.519486911985595] },
  // ];

  // console.log(makeGraph(points));

  const handleAddNewPoint = () => {
    alert('Щоб продовжити, виберіть нову точку на мапі');
    setAddingNewPointMode(true)
  }

  const handleMapClick = (event: any, map: any) => {
    if (isAddingNewPointMode) {
      map.flyTo(event.latlng, map.getZoom());
      // eslint-disable-next-line
      if (confirm('Далі?')) {
        console.log(event);
        navigate(`/create-new-point?lat=${event.latlng.lat}&lng=${event.latlng.lng}`)
      }
    };
    if (isShowRouteMode) {
      if (!startPoint) {
        setStartPoint(event.latlng);
        alert('Виберіть точку призначення');
        return;
      }
      if (!endPoint) {
        setEndPoint(event.latlng);
        return;
      }
    }
  }

  const handleRouteCancel = () => {
    setRouteMode(false);
    setStartPoint(undefined);
    setEndPoint(undefined);
  }

  const handleRouteBuild = () => {
    alert('Виберіть початок маршруту');
    setRouteMode(true)
  }

  console.log(points);

  return (
    <div>
      {!points.length && <div style={{display: "flex", margin: 20, alignItems: 'center', justifyContent: 'center'}}>Завантаження даних карти...</div>}
    <div style={{display: "flex", margin: 20, alignItems: 'center', justifyContent: 'center'}}>
      {isAddingNewPointMode ? <Button type='back' onClick={() => setAddingNewPointMode(false)}>Відмінити</Button>
        : <Button type='success' onClick={handleAddNewPoint}>Додати точку</Button>}
      {isShowRouteMode ? <Button style={{marginLeft: 20}} type='back' onClick={handleRouteCancel}>Відмінити</Button>
        : <Button style={{marginLeft: 20}} type='default' onClick={handleRouteBuild}>Побудувати маршрут</Button>}
    </div>
    <div style={{height: 500, width: 500}} id="map">
      <MapContainer center={[50.46869871698446, 30.515297493199174]} zoom={13} scrollWheelZoom={false}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {points.map((point, i) => (
          <Marker position={[point.latitude, point.longitude]} icon={getMarkerIcon(point.title)} key={i}>
            <Popup>
              {point.title}
            </Popup>
          </Marker>
        ))}
        {startPoint && (
          <Marker position={[startPoint.lat, startPoint.lng]} icon={getRouteMarkerIcon()}>
            <Popup>
              Початок маршруту
            </Popup>
          </Marker>
        )}
        {endPoint && (
          <Marker position={[endPoint.lat, endPoint.lng]} icon={getRouteMarkerIcon()}>
            <Popup>
              Точка призначення
            </Popup>
          </Marker>
        )}
        {(startPoint && endPoint) && <RoutingMachine startPoint={startPoint} endPoint={endPoint} />}
        <MapClickEvents onMapClick={handleMapClick} />
      </MapContainer>
    </div>
    </div>
  )
}