import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('activo', function() {
    this.route('create');
    this.route('edit', {path: '/activo/edit/:id'});
  });
});

export default Router;
