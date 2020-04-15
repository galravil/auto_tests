import { Selector } from 'testcafe'
import LoginPage from '../pages/loginPage'
import { baseUser } from '../data/users'


fixture `Getting Started`
    .page `http://devexpress.github.io/testcafe/example`
    .beforeEach( async t => {
        /* test initialization code */
    })
    .afterEach( async t => {
        /* test finalization code */
    });


    test('Login', async t => {
        await LoginPage.openPage()
        await LoginPage.login(baseUser.login, baseUser.password)
    })
