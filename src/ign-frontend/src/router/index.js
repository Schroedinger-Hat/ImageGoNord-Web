import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import GettingStarted from '../views/GettingStarted.vue';
import Documentation from '../views/Documentation.vue';
import About from '../views/About.vue';
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
    path: '/documentation/python',
    name: 'Documentation Python',
    component: Documentation,
  },
  {
    path: '/documentation/api',
    name: 'Documentation API',
    component: Documentation,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/*',
    name: '404',
    component: Error404,
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
