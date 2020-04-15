import { Selector, t } from 'testcafe';
import { URLS } from '../data/urls'


class LoginPage {
    constructor () {
        this.loginInput    = Selector('input[type="email"]');
        this.passwordInput = Selector('input[type="password"]');
        this.signInButton  = Selector('button.btn.btn-lg.btn-primary.pull-xs-right');
    }

    async openPage() {
        await t
            .navigateTo(URLS.login)
    }

    async login(login, password) {
        await t
            .typeText(this.loginInput, login)
            .typeText(this.passwordInput, password)
            .click(this.signInButton)

    }
}

export default new LoginPage()