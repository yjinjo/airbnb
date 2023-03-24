export interface IRoomCategory {
  name: string;
  kind: string;
}

export interface IRoomPhotoPhoto {
  pk: string;
  file: string;
  description: string;
}

export interface IRoomList {
  pk: number;
  name: string;
  country: string;
  city: string;
  price: number;
  rating: number;
  is_owner: boolean;
  photos: IRoomPhotoPhoto[];
  category: IRoomCategory;
}

export interface IRoomOwner {
  name: string;
  avatar: string;
  username: string;
}

export interface IAmenity {
  pk: number;
  name: string;
  description: string;
}

export interface IRoomDetail extends IRoomList {
  created_at: string;
  updated_at: string;
  rooms: number;
  toilets: number;
  description: string;
  address: string;
  pet_friendly: true;
  kind: string;
  is_owner: boolean;
  is_liked: boolean;
  category: ICategory;
  owner: IRoomOwner;
  amenities: IAmenity[];
  rating: number;
  id: number;
}

export interface ICategory {
  pk: number;
  name: string;
  kind: string;
}

export interface IReview {
  payload: string;
  rating: number;
  user: IRoomOwner;
}

export interface IUser {
  last_login: string;
  username: string;
  email: string;
  date_joined: string;
  avatar: string;
  name: string;
  is_host: boolean;
  gender: string;
  language: string;
  currency: string;
}

export interface IBooking {
  id: number;
  room: {
    name: string;
    price: number;
  };
  kind: string;
  check_in: string;
  check_out: string;
  guests: number;
  not_canceled: boolean;
}
