import { StreetType } from '../street-type';

export interface AdjacentStreet {
  name: any;
  type: StreetType|null;
  id: string|null;
}