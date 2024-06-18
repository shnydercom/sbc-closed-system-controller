import { emptySplitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    accelerometerGyroSensor: build.query<
      AccelerometerGyroSensorApiResponse,
      AccelerometerGyroSensorApiArg
    >({
      query: () => ({ url: `/rest/accelerometer-gyro-sensor` }),
    }),
    currentSensor: build.query<CurrentSensorApiResponse, CurrentSensorApiArg>({
      query: () => ({ url: `/rest/current-sensor` }),
    }),
    pantiltOrientation: build.query<
      PantiltOrientationApiResponse,
      PantiltOrientationApiArg
    >({
      query: () => ({ url: `/rest/pantilt-orientation` }),
    }),
    panToMin: build.query<PanToMinApiResponse, PanToMinApiArg>({
      query: () => ({ url: `/rest/pan-to-min` }),
    }),
    panToMiddle: build.query<PanToMiddleApiResponse, PanToMiddleApiArg>({
      query: () => ({ url: `/rest/pan-to-middle` }),
    }),
    panToMax: build.query<PanToMaxApiResponse, PanToMaxApiArg>({
      query: () => ({ url: `/rest/pan-to-max` }),
    }),
    panBy: build.query<PanByApiResponse, PanByApiArg>({
      query: (queryArg) => ({ url: `/rest/pan-by/${queryArg.relativeangle}` }),
    }),
    tiltToMin: build.query<TiltToMinApiResponse, TiltToMinApiArg>({
      query: () => ({ url: `/rest/tilt-to-min` }),
    }),
    tiltToMiddle: build.query<TiltToMiddleApiResponse, TiltToMiddleApiArg>({
      query: () => ({ url: `/rest/tilt-to-middle` }),
    }),
    tiltToMax: build.query<TiltToMaxApiResponse, TiltToMaxApiArg>({
      query: () => ({ url: `/rest/tilt-to-max` }),
    }),
    tiltBy: build.query<TiltByApiResponse, TiltByApiArg>({
      query: (queryArg) => ({ url: `/rest/tilt-by/${queryArg.relativeangle}` }),
    }),
    readIndex: build.query<ReadIndexApiResponse, ReadIndexApiArg>({
      query: () => ({ url: `/` }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as rtkQueryClientApi };
export type AccelerometerGyroSensorApiResponse =
  /** status 200 Successful Response */ AccelerometerGyroSensorReading;
export type AccelerometerGyroSensorApiArg = void;
export type CurrentSensorApiResponse =
  /** status 200 Successful Response */ Ina219SensorReading;
export type CurrentSensorApiArg = void;
export type PantiltOrientationApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type PantiltOrientationApiArg = void;
export type PanToMinApiResponse = /** status 200 Successful Response */ PanTilt;
export type PanToMinApiArg = void;
export type PanToMiddleApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type PanToMiddleApiArg = void;
export type PanToMaxApiResponse = /** status 200 Successful Response */ PanTilt;
export type PanToMaxApiArg = void;
export type PanByApiResponse = /** status 200 Successful Response */ PanTilt;
export type PanByApiArg = {
  relativeangle: number;
};
export type TiltToMinApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type TiltToMinApiArg = void;
export type TiltToMiddleApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type TiltToMiddleApiArg = void;
export type TiltToMaxApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type TiltToMaxApiArg = void;
export type TiltByApiResponse = /** status 200 Successful Response */ PanTilt;
export type TiltByApiArg = {
  relativeangle: number;
};
export type ReadIndexApiResponse = /** status 200 Successful Response */ any;
export type ReadIndexApiArg = void;
export type AccelerometerGyroSensorReading = {
  acceleration: [number, number, number];
  gyro: [number, number, number];
};
export type Ina219SensorReading = {
  vin_plus_voltage: number;
  bus_voltage: number;
  shunt_voltage: number;
  current: number;
  powerCalc: number;
  powerRegister: number;
};
export type PanTilt = {
  pan?: number;
  tilt?: number;
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export const {
  useAccelerometerGyroSensorQuery,
  useCurrentSensorQuery,
  usePantiltOrientationQuery,
  usePanToMinQuery,
  usePanToMiddleQuery,
  usePanToMaxQuery,
  usePanByQuery,
  useTiltToMinQuery,
  useTiltToMiddleQuery,
  useTiltToMaxQuery,
  useTiltByQuery,
  useReadIndexQuery,
} = injectedRtkApi;
