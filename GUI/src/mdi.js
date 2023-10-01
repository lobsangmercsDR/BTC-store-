import * as mdiIcons from '@mdi/js';

const install = (app) => {
  Object.keys(mdiIcons).forEach((iconName) => {
    app.component(iconName, {
      template: `<mdi-icon path="${mdiIcons[iconName]}"></mdi-icon>`,
    });
  });
};

export default {
  install,
};
