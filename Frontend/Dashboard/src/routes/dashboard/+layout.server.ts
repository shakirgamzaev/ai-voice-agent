import type { LayoutServerLoad } from './$types';

export const prerender = false;

// Track the pathname so dashboard page changes also run the server hook's session check.(TODO in produ): Maybe since any dashboad/* route will send a request to fetch the data to the server, maybe i should disable this later. I am keeping this at the moment
export const load: LayoutServerLoad = ({ url }) => ({ pathname: url.pathname });
