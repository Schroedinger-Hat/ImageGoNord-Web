import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import GettingStarted from '../views/GettingStarted.vue';
import Documentation from '../views/Documentation.vue';
import Installation from '../views/Installation.vue';
import Error404 from '../views/Error404.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/getting-started',
    name: 'GettingStarted',
    component: GettingStarted,
  },
  {
    path: '/installation',
    name: 'Installation',
    component: Installation,
  },
  {
    path: '/documentation',
    name: 'Documentation',
    component: Documentation,
  },
  {
    path: '/*',
    name: '404',
    component: Error404,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
